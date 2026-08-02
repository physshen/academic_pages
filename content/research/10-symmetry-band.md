---
widget: blank
active: true
headless: true
weight: 10

title: Probing symmetry breaking orders

design:
  columns: '1'
  background:
    # `color` shows through wherever the image is missing or still loading,
    # so the band looks intentional even before a photo is added.
    color: '#1b3a6b'
    # Path is relative to `static/media/`, i.e. this resolves to /media/SHG.png
    image: 'SHG.png'
    # Light overlay so the figure stays visible; legibility of the white title
    # comes from the text-shadow in `advanced.css_style` below rather than from
    # dimming the whole image.
    image_darken: 0.1
    image_size: cover
    image_position: center
    image_parallax: false
    text_color_light: true
  spacing:
    padding: ['130px', '0', '130px', '0']

advanced:
  # text-shadow is inherited, so setting it on the section reaches the title.
  # Layered shadow acts as a soft dark plate behind the glyphs, which is what
  # keeps the white title readable now that the overlay is nearly transparent.
  css_style: 'text-shadow: 0 2px 4px rgba(0,0,0,0.9), 0 0 18px rgba(0,0,0,0.9), 0 0 42px rgba(0,0,0,0.7);'
---
