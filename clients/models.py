from django.db import models
from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO


class Client(models.Model):
    image = models.ImageField(upload_to='clients/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    designation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name
    
    def crop_image(self, target_width=450, target_height=350):
        """Crop and resize image to exact dimensions"""
        if not self.image:
            return
        
        # Open the image from the file
        if hasattr(self.image, 'file'):
            # New upload - read from file object
            self.image.file.seek(0)
            img = Image.open(self.image.file)
        else:
            # Existing file - open from path
            img = Image.open(self.image.path)
        
        # Convert RGBA to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = rgb_img
        
        # Get original dimensions
        original_width, original_height = img.size
        
        # Calculate aspect ratios
        target_aspect = target_width / target_height
        original_aspect = original_width / original_height
        
        # Resize maintaining aspect ratio to cover target size
        if original_aspect > target_aspect:
            # Image is wider - fit to height
            new_height = target_height
            new_width = int(original_width * (target_height / original_height))
        else:
            # Image is taller - fit to width
            new_width = target_width
            new_height = int(original_height * (target_width / original_width))
        
        # Resize image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Crop from center to exact target size
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2
        
        img = img.crop((int(left), int(top), int(right), int(bottom)))
        
        # Save to BytesIO
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=95, optimize=True)
        img_io.seek(0)
        
        # Get the original filename
        if hasattr(self.image, 'name') and self.image.name:
            filename = os.path.basename(self.image.name)
            name, ext = os.path.splitext(filename)
        else:
            name = 'image'
        
        # Replace the image file with cropped version
        self.image.save(
            f"{name}.jpg",
            ContentFile(img_io.read()),
            save=False
        )
    
    def save(self, *args, **kwargs):
        # Crop image if it exists (new upload or changed)
        if self.image:
            # Check if this is a new upload or image change
            if not self.pk:
                # New instance - crop the image
                self.crop_image()
            else:
                # Existing instance - check if image changed
                try:
                    old_instance = Client.objects.get(pk=self.pk)
                    # If image name changed or file object exists, it's a new upload
                    if not old_instance.image or old_instance.image.name != self.image.name or hasattr(self.image, 'file'):
                        self.crop_image()
                except Client.DoesNotExist:
                    self.crop_image()
        
        super().save(*args, **kwargs)
