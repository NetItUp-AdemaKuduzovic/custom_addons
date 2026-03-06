/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("services").add(
    "studio",
    {
        start() {
            return {
                open: async () => {},
                close: async () => {},
                ready: Promise.resolve(),
                isStudioEditable: () => false,
                isStudioActive: () => false,
            };
        },
    },
    { force: true }
);