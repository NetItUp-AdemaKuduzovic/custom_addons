/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("services").add(
    "studio",
    {
        start() {
            return {
                open: async () => {},
                leave: async () => {},
                isStudioEditable: () => false,
            };
        },
    },
    { force: true }
);