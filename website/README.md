# Headbangers Ball Archive - Website

The official website for the Headbangers Ball Archive, built with Jekyll and deployed to GitHub Pages.

## Live Site

🌐 **https://realjbmangum.github.io/headbanger/**

## Local Development

### Prerequisites

- Ruby 3.4+ (via Homebrew recommended)
- Bundler

### Setup

1. Install Ruby via Homebrew (if not already installed):
```bash
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
```

2. Install dependencies:
```bash
bundle install
```

3. Generate episode data from CSV:
```bash
python3 scripts/csv_to_yaml.py
```

4. Build and serve the site locally:
```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

### Building for Production

To build the site without serving:
```bash
bundle exec jekyll build
```

The generated site will be in the `_site/` directory.

## Project Structure

```
website/
├── _config.yml           # Jekyll configuration
├── _layouts/            # Page templates
│   ├── default.html     # Base layout
│   └── episode.html     # Episode detail layout
├── _episodes/           # Generated episode markdown files (455 files)
├── _data/              # Data files
│   ├── stats.yml       # Statistics
│   └── episodes.yml    # Episode data
├── assets/
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── js/
│       └── main.js     # JavaScript functionality
├── scripts/
│   └── csv_to_yaml.py  # Data conversion script
├── index.html          # Homepage
├── episodes.html       # Episode browser
├── stats.html         # Statistics page
├── about.html         # About page
└── Gemfile            # Ruby dependencies
```

## Features

- **455 Episodes**: Complete archive with detailed metadata
- **Advanced Filtering**: Search and filter by year, era, host
- **Statistics Dashboard**: Comprehensive stats and visualizations
- **Responsive Design**: Optimized for all devices
- **Dark Metal Theme**: Custom design with neon accents
- **Fast & Secure**: Static site generation with Jekyll
- **SEO Optimized**: Jekyll SEO plugin with proper metadata

## Deployment

The site automatically deploys to GitHub Pages via GitHub Actions on every push to `main`.

### Manual Deployment

If needed, you can trigger a manual deployment from the GitHub Actions tab.

### Deployment Configuration

The workflow is defined in `.github/workflows/jekyll.yml` and:
- Builds the Jekyll site with Ruby 3.4
- Uploads the artifact to GitHub Pages
- Deploys to the production environment

## Data Updates

When episode data is updated:

1. Update `data/episodes.csv` in the root directory
2. Regenerate Jekyll data:
   ```bash
   python3 scripts/csv_to_yaml.py
   ```
3. Commit and push changes
4. GitHub Actions will automatically rebuild and deploy

## Design System

### Colors
- Background: `#0A0A0A` (Dark)
- Primary: `#00D9FF` (Electric Blue)
- Secondary: `#FF006E` (Hot Pink)
- Accent: `#39FF14` (Neon Green)

### Typography
- Display: Permanent Marker
- Body: Inter

### Components
- Episode cards with hover effects
- Stat cards with animations
- Responsive navigation
- Filterable grids

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

Data compiled for historical and educational purposes.
MTV and Headbangers Ball are trademarks of their respective owners.

---

🤘 Built with Jekyll and deployed via GitHub Pages
