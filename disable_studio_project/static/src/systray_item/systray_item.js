/** @odoo-module **/

import * as studioSystrayModule from '@web_studio/systray_item/systray_item';
import { patch } from "@web/core/utils/patch";

patch(studioSystrayModule.systrayItem, {
    isDisplayed: () => false,
});