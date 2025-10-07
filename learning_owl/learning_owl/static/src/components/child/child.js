import { Component, onWillStart, onWillDestroy, useState } from "@odoo/owl";

export class Child extends Component {
    static template = "learning_owl.child";
    static props = {
        title: { type: String },
        list: { type: Array },
        slots: { type: Object },
        counter: { type: Number },
    };

    setup() {
        onWillStart(() => console.log("Child on onWillStart hook"));
        onWillDestroy(() => alert("Destroyed child component? "));
    }

}