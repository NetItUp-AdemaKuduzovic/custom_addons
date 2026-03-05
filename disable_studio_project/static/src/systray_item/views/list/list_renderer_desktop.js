import { patch } from "@web/core/utils/patch";
import { ListRenderer } from '@web/views/list/list_renderer';

patch(ListRenderer.prototype, {
    isStudioEditable: () => false,
})