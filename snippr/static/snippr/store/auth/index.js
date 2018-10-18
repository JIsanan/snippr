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
    if(payload) {
      state.token = payload
      localStorage.setItem('token', payload);
      //axios.defaults.headers.common['Authorization'] = state.token;
    }
  },
  setRefresh(state, payload){
    if(payload) {
      localStorage.setItem('refresh', payload);
    }
  },
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
      commit('setToken', response.access);
      commit('setRefresh', response.refresh);
      return response;
    }).catch(response => {
      console.error(response);
    });
  },
  async refreshLogin({commit}){
      let token = localStorage.getItem('token')
      if(token) {
        commit('setToken', token);
      }
      
      return token;
  },

};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};
