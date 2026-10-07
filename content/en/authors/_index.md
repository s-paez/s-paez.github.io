---
# Keep author data available to templates without publishing duplicate bios.
build:
  render: never
cascade:
  build:
    render: never
    list: always
    publishResources: false
---
