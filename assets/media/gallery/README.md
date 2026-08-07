# Gallery photos

Drop `.jpg` / `.png` / `.webp` files in this folder and they show up on
`/gallery/`, two across, ordered by filename. Prefix names to control the order:

    10-perovskite.jpg
    20-terahertz.jpg
    30-cryostat.jpg

Hugo generates a display copy sized to the column width (800px at two columns)
and a 2400px lightbox copy, keeping each photo's own aspect ratio — nothing is
cropped, so it is fine to drop in full-resolution originals. They are never
served as-is.

The words under each photo go in `data/gallery.yaml`, keyed by filename. See the
examples in that file for the short (one line) and long (heading + paragraph)
forms.

To change how many photos sit across, edit the `columns` value in
`content/gallery/_index.md` — `"1"` gives one big photo per row, `"3"` a tighter
grid. Any setting collapses to a single column on phones.
