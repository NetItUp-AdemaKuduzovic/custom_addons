import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Child } from "../child/child";
import { useService } from "@web/core/utils/hooks";

export class Example extends Component {
    static template = "learning_owl.example_owl_template";
    static components = { Child };

    setup() {
        this.message = "Hello there";
        this.state = useState({ counter: 0 });
    }

    alertMessage(event) {
        alert(this.message);
    }

    increment(event) {
        this.state.counter++;
    }
}

registry.category("view_widgets").add("example", { component: Example });