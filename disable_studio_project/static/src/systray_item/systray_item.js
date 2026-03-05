/** @odoo-module **/

import { registry } from "@web/core/registry";

const systray = registry.category("systray");

const original = systray.get("StudioSystrayItem");

systray.add("StudioSystrayItem", {
    ...original,
    setup() {
        super.setup();
    },
    // Use this if: optionally show only in debug mode for system users:
    // isDisplayed: () => odoo.debug && user.isSystem
    isDisplayed: () => false
}, { force: true });