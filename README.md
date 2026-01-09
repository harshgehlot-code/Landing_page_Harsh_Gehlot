# Frontend Structure

This directory contains the frontend assets for the Real Trust landing page.

## Directory Structure

```
frontend/
├── templates/
│   └── index.html          # Main landing page template
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── js/
│   │   └── main.js         # JavaScript for API integration
│   └── images/             # SVG images and assets
│       ├── *.svg           # Icons, shapes, and images
└── README.md               # This file
```

## Files Description

### Templates
- **index.html**: Main landing page template using Django template tags for static files

### Static Files

#### CSS (`static/css/`)
- **style.css**: Contains all custom styles including:
  - CSS variables for colors
  - Navigation styles
  - Hero section styles
  - Card styles for projects and clients
  - Form styles
  - Responsive design

#### JavaScript (`static/js/`)
- **main.js**: Contains all JavaScript functionality:
  - API integration (fetch API)
  - Projects loading
  - Clients loading
  - Contact form submission
  - Newsletter subscription
  - Error handling
  - XSS protection

#### Images (`static/images/`)
- SVG icons (circle-dollar-sign.svg, paintbrush-2.svg, home.svg, etc.)
- SVG images (pexels images, shapes, etc.)
- All decorative elements

## Usage

The frontend is integrated with Django and uses Django's static file system:

1. Templates are served from `frontend/templates/`
2. Static files are served from `frontend/static/`
3. Django's `{% static %}` tag is used to reference static files
4. Images can be referenced using `{% static 'images/filename.svg' %}`

## API Integration

The frontend communicates with the Django REST API:

- **GET /api/projects/** - Fetches all projects
- **GET /api/clients/** - Fetches all clients
- **POST /api/contacts/** - Submits contact form
- **POST /api/newsletter/** - Subscribes to newsletter

All API calls use the Fetch API with proper error handling.

## Development

To add new static files:
1. Place CSS files in `static/css/`
2. Place JavaScript files in `static/js/`
3. Place images in `static/images/`
4. Reference them in templates using `{% static 'path/to/file' %}`

## Notes

- All images should be optimized SVGs when possible
- JavaScript uses modern ES6+ syntax
- CSS uses CSS variables for easy theming
- Bootstrap 5.3.2 is loaded via CDN
- Bootstrap Icons are loaded via CDN

