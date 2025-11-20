# Project Detail Pages - Content Guide

Each project in `app/content/projects.json` can now include detailed information for the project detail pages.

## Required Fields

- `id`: Unique identifier (used in URL, e.g., `/projects/cactus-tapestry`)
- `title`: Project name
- `description`: Short description (shown on project cards)
- `image`: Main hero image path (use WebP format if possible, e.g., `/static/img/image.webp`)
- `category`: "Crochet", "Knitting", or "Sewing"

## Optional Fields for Detail Pages

### Basic Info
- `pattern_info`: Where you got the pattern (e.g., "Pattern by [Designer]", "Self-drafted", "Free pattern on Ravelry")
- `pattern_link`: URL to the pattern (if available)
- `time_taken`: How long it took (e.g., "2 weeks", "10 hours", "1 weekend")

### Content
- `narrative`: Array of paragraphs telling the story of making this project
  ```json
  "narrative": [
    "First paragraph about inspiration or starting the project...",
    "Second paragraph about the process...",
    "Third paragraph about challenges or final thoughts..."
  ]
  ```
  
  OR use the simple `content` field for a single paragraph (backward compatible)

### Tips & Tricks
- `tips`: Can be a string OR an array of strings
  ```json
  "tips": "Single tip as a string"
  ```
  OR
  ```json
  "tips": [
    "First helpful tip",
    "Second helpful tip",
    "Third helpful tip"
  ]
  ```

- `challenges`: Array of challenges you faced
  ```json
  "challenges": [
    "Managing multiple yarn colors was tricky",
    "The shaping was more complex than expected"
  ]
  ```

- `helpful_tips`: Array of things you wish you'd known
  ```json
  "helpful_tips": [
    "Start with a gauge swatch",
    "Use stitch markers liberally"
  ]
  ```

### Images
- `additional_images`: Array of image paths for the gallery
  ```json
  "additional_images": [
    "/static/img/project-detail-1.webp",
    "/static/img/project-detail-2.webp"
  ]
  ```

## Example Project Entry

```json
{
  "id": "my-project",
  "title": "My Amazing Project",
  "description": "A beautiful handmade piece",
  "image": "/static/img/my-project.webp",
  "category": "Crochet",
  "pattern_info": "Pattern by Jane Designer",
  "pattern_link": "https://example.com/pattern",
  "time_taken": "2 weeks",
  "tips": [
    "Use stitch markers",
    "Check gauge first"
  ],
  "challenges": [
    "The color changes were tricky",
    "Had to redo the border three times"
  ],
  "helpful_tips": [
    "Blocking makes a huge difference",
    "Take photos as you go for reference"
  ],
  "narrative": [
    "I started this project because...",
    "The most interesting part was...",
    "I'm so happy with how it turned out!"
  ],
  "additional_images": [
    "/static/img/my-project-2.webp",
    "/static/img/my-project-3.webp"
  ]
}
```

## How to Add a New Project

1. Add your images to `app/static/img/`.
2. **Optimization**: Run `python scripts/optimize_images.py` to automatically resize images and convert them to WebP format for better performance.
3. Add a new entry to `app/content/projects.json` with at least the required fields.
4. The project will automatically appear on the Projects page and be clickable.
5. Fill in the optional fields to create a rich detail page.

## Blog Posts Content Guide

Blog posts are stored in `app/content/blog.json`.

### Structure
```json
{
  "slug": "url-friendly-slug",
  "title": "Post Title",
  "subtitle": "Optional Subtitle",
  "date": "YYYY-MM-DD",
  "content": "Full text content with newlines for paragraphs...",
  "image": "/static/img/blog-image.webp"
}
```

### Updating Content
To update blog post content efficiently without breaking JSON formatting, you can use the provided script:
1. Edit `scripts/update_blog_content.py` with your new text.
2. Run `python scripts/update_blog_content.py`.
This handles escaping characters and formatting automatically.
