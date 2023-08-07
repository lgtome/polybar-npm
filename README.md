# Script for polybar to get npm packages

This script displays the current selected npm packages. Information is obtained from npm official api.

![BarExample](assets/example.png)

# Python Dependencies

-   `argparser`
-   `requests`
-   `configparser`

# Usage

Move `pnpm.py` and `pnpm.config` to specific folder and create polybar module or use `install.sh` script.

# Polybar import module

You just need to import module ( if you installed it from script or manually as file ):
- go to your polybar conf file with the bars
- use `include-file` on the top of file
- `include-file = path/to/your/module/or/modules/file`

# Config

Exist config has predefined options:

-   react
-   vue
-   leaflet
-   graphql
-   pg
-   amqplib
-   sass
-   less
-   stylus
-   ember-cli
-   svelte
-   electron
-   angular

You can use these options, or create your own, just add a section to the config like this:

```
[FRAMEWORK_NAME]
name = FRAMEWORK_NPM_NAME
icon = FRAMEWORK_ICON
```
