import axios from 'source/plugins/axios';
import router from 'source/router/index';

const state = {
  token: null,
};

const getters = {
  token: state => state.token,

  isLoggedIn(state) {
    return state.token != null;
  }
};

const mutations = {
  setToken(state, payload){
  console.log(payload)
    if(payload) {
      state.token = payload.access
      localStorage.setItem('token', payload.access);
      localStorage.setItem('refresh', payload.refresh);
      axios.defaults.headers.common['Authorization'] = state.token;
    }
  }

};

const actions = {
  createUser({commit}, data) {
    return axios.post('api/register/',
      data
    ).then(response => {
      return response;
    });
  },
  removeJWT() {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh');
    state.token = null;
    return "success";
  },
  tryLogIn({commit}, data) {
    return axios.post('api/token/',
      data
    ).then(response => {
      commit('setToken', response);
      return response;
    }).catch(response => {
      console.error(response);
    });
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};
