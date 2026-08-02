---
widget: blank
active: true
headless: true
weight: 30

title: Engineering quantum phases

design:
  columns: '1'
  background:
    color: '#1b3a6b'
    # Landau double well, order parameter driven over the barrier into the
    # metastable minimum. Regenerate with `python3 scripts/gen_landau.py`.
    image: 'headers/landau.svg'
    # The artwork carries its own ground, so brightness is tuned in the SVG
    # gradient rather than here; this stays near zero.
    image_darken: 0.05
    image_size: cover
    image_position: center
    image_parallax: false
    text_color_light: true
  spacing:
    padding: ['130px', '0', '130px', '0']

advanced:
  css_style: 'text-shadow: 0 2px 4px rgba(0,0,0,0.9), 0 0 18px rgba(0,0,0,0.9), 0 0 42px rgba(0,0,0,0.7);'
---
