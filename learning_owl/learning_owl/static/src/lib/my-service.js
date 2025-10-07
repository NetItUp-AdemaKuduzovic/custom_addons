import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

registry.category("services").add("my-service", {
    dependencies: ["notification"],
    start(env, { notification }) {
        setInterval(() => notification.add("Hello"), 500000);
    }
})