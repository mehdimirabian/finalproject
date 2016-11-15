// This is the js for the default/index.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };



/*

    self.show_cancel = function() {
      if(self.vue.is_adding_info || self.vue.is_editing_info){
          return true;
      }
      else {
          return false;
      }
    };

    self.show_add = function() {
        if(!self.vue.is_adding_info && !self.vue.has_info_been_added){
            alert(true);
            return true;
        }
        else
            alert(false);
            return false;
    };

    self.show_edit = function () {
        if(!self.vue.is_adding_info && self.vue.has_info_been_added){
            return true;
        }

        else {
            return false;
        }
    };

   */

    self.add_info_button = function () {
        // The button to add a track has been pressed.
        self.vue.is_adding_info = !self.vue.is_adding_info;

    };

    self.edit_info_button = function () {
        self.vue.is_editing_info = !self.vue.is_editing_info;
    };

    self.add_info = function () {
        // The submit button to add a track has been added.
        self.vue.has_info_been_added = true;
        $.post(add_info_url,
            {
                skills: self.vue.form_skills,
                available_times: self.vue.form_available_times
            },
            function (data) {
                $.web2py.enableElement($("#add_info_submit"));
                self.vue.info.unshift(data.info);
            });
    };


    self.edit_info = function (info_id) {
        alert(info_id);
        $.post(edit_info_url,
            {
                info_id: info_id,
                skills: self.vue.form_skills,
                available_times: self.vue.form_available_times
            },
            function (data) {
                $.web2py.enableElement($("#edit_info_submit"));
                self.vue.info.unshift(data.info);
                // data.info.editable = true;
                // self.vue.info.splice(idx, 1, data.info);
            });
    };



    self.vue = new Vue({
        el: "#vue-div",
        data: {
            is_adding_info: false,
            has_info_been_added: false,
            is_editing_info: false,
            info: [],
            logged_in: false,
            form_skills: null,
            form_available_times: null
        },
        methods: {
            add_info_button: self.add_info_button,
            add_info: self.add_info,
            edit_info_button: self.edit_info_button,
            edit_info: self.edit_info

        }

    });

    $("#vue-div").show();


    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
