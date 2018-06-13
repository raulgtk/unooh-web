function CookieEngine() {

    var DOM = {},
        LAW = {},
        UTILS = {},
        LIBS = {},
        ERROR = {},
        COOKIES = {},
        doc = document,
        win = window,
        isDebug = true,
        cookieEngine = this,
        requirements = [
            '//cdnjs.cloudflare.com/ajax/libs/postscribe/2.0.8/postscribe.min.js'
        ];

    DOM.getId = function(str) {

        return doc.getElementById(str); 
    };

    DOM.getClass = function(str) {

        return doc.getElementsByClassName(str);
    };

    DOM.create = function(tag) {

        return doc.createElement(tag);
    };

    DOM.append = function(target, ele) {

        target.appendChild(ele);
    };

    DOM.remove = function(target) {

        target.parentElement.removeChild(target);
    };

    DOM.getContent = function(ele) {

        return ele.textContent;
    };

    DOM.replace = function(target) {

        var remove = DOM.remove,
            getContent = DOM.getContent,
            content = getContent(target),
            parent = target.parentNode,
            trace = UTILS.trace;

        postscribe(parent, content);
        remove(target);
    };

    LAW.consent = function() {

        var replace = DOM.replace,
            getClass = DOM.getClass,
            consent = LAW.consent,
            debounce = UTILS.debounce,
            items = getClass('cookie-consent'),
            trace = UTILS.trace;

        if (typeof(postscribe) == 'undefined') {
            debounce(consent);
        } else {
            while (items.length) {
                replace(items[0]);
            }
        }
    };

    LAW.refuse = function() {

        var trace = UTILS.trace;

        trace("Refused!");
    };

    LIBS.requirements = function() {

        var create = DOM.create,
            append = DOM.append,
            target = doc.head,
            ele, i;

        for (i = 0; i < requirements.length; i++) {
            ele = create('script');
            ele.type = 'text/javascript';
            ele.src = requirements[i];
            append(target, ele);
        }
    };

    ERROR.exception = function(str) {

        throw str || 'Error';
    };

    UTILS.debounce = function(callback) {

        setInterval(callback, 100);
    };

    UTILS.addListener = function(event, obj, callback) {

        if (obj.addEventListener) {
            obj.addEventListener(event, callback, false);
        } else {
            obj.attachEvent('on' + event, callback);
        }
    };

    UTILS.trace = function() {

        var args = arguments,
            msg = [];

        for (var i = 0; i < args.length; i++) {
            msg.push(args[i]);
        }
        if (isDebug && win.console) {
            console.log(msg);
        }
    };

    cookieEngine.init = function(accept) {

        var getId = DOM.getId,
            consent = LAW.consent,
            refuse = LAW.refuse,
            exception = ERROR.exception,
            requirements = LIBS.requirements,
            addListener = UTILS.addListener,
            acceptBtn = getId('cookie-accept-btn'),
            refuseBtn = getId('cookie-refuse-btn'),
            trace = UTILS.trace;

        requirements();
        if (accept === undefined) {
            addListener("click", acceptBtn, consent);
            addListener("click", refuseBtn, refuse);
        } else if (accept === true) {
            consent();
        } else if (accept === false) {
            refuse();
        } else {
            exception("Initialize Error");
        }
    };
}

new CookieEngine().init();