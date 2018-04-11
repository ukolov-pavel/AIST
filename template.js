<template id='JS'>
  <script type="text/javascript">
    var errorObj = {
    _errors : [],

    addError : function(message, source, lineno) {
        this._errors.push(
            "Message: " + message + "\n" +
            "Source: " + source + "\n" +
            "Line: " + lineno
        );
    },

    getErrors : function() {
        return this._errors;
        }
    }

    window.onerror =  function(message, source, line_no) {
        errorObj.addError(message, source, line_no);
    }
  </script>
</template>