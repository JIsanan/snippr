import Vue from 'vue';
import Vuex from 'vuex';
import auth from 'source/store/auth';
import user from 'source/store/user';

Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
        auth,
        user
    }
});

export default store;
