---
widget: blank
active: true
headless: true
weight: 10

title: Probing symmetry breaking orders

design:
  columns: '1'
  background:
    # SHG.png is transparent around the figure, so `color` is the band's
    # ground. Kept light (the same on all three research bands) so the
    # figure's black axes and labels stay visible.
    color: '#e8f0fa'
    # Path is relative to `static/media/`, i.e. this resolves to /media/SHG.png
    image: 'SHG.png'
    # No overlay: it would grey the light ground. Title legibility comes from
    # the text-shadow in `advanced.css_style` below.
    image_darken: 0
    image_size: cover
    image_position: center
    image_parallax: false
    text_color_light: false
  spacing:
    padding: ['130px', '0', '130px', '0']

advanced:
  # text-shadow is inherited, so setting it on the section reaches the title.
  # Layered white glow acts as a soft light plate behind the dark glyphs where
  # the title crosses the figure.
  css_style: 'text-shadow: 0 0 4px #fff, 0 0 14px #fff, 0 0 32px rgba(255,255,255,0.9);'
---
