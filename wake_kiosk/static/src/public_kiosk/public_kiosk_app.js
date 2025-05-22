/** @odoo-module **/

import App from '@hr_attendance/public_kiosk/public_kiosk_app';
import { patch } from "@web/core/utils/patch";
import { onWillDestroy } from "@odoo/owl";

patch(App.kioskAttendanceApp.prototype, {

    setup() {
        super.setup()

        this.keepaliveTimer = null;

        this.minTime = 2 * 60 * 1000;
        this.maxTime = 5 * 60 * 1000;
        this.workingHours = [
            { start:7, end:10 },
            { start:12, end:15 },
            { start:17, end:19 }
        ];

        this._keepAlive();

        //Prevents memory leaks
        onWillDestroy(() => {
            if (this.keepaliveTimer) {
                clearTimeout(this.keepaliveTimer);
                this.keepaliveTimer = null;
            }
        });
    },

    _areWorkingHours() {
        const currHour = new Date().getHours();

        return this.workingHours.some(frame => 
            currHour >= frame.start && currHour <= frame.end
        );
    },

    _keepAlive() {
        if(this._areWorkingHours()){
            fetch('/hr_attendance/kiosk_keepalive?' + new Date().getTime().toString(), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                },
            });
        }

        const randomTime = Math.floor(Math.random() * (this.maxTime - this.minTime + 1)) + this.minTime;

        this.keepaliveTimer = setTimeout(() => {
            this._keepAlive();
        }, randomTime);
    }
})