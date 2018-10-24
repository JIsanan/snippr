import axios from 'source/plugins/axios';
import router from 'source/router/index';

const state = {
  token: localStorage.getItem('token') || null,
  user: null
};

const getters = {
  token: state => state.token,

  getUser(state) {
    return state.user;
  },

  isLoggedIn(state) {
    return state.token != null;
  }
};

const mutations = {
  setUser(state, payload){
    if(payload) {
      state.user = payload
    }
  },
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
  verifyJWT({commit}, data){
    return axios.post('api/token/verify/',
      data
    ).then(response => {
      console.log(response)
    }).catch(response => {
      console.error(response);
    })
  },
  refreshJWT({commit}, data){
    return axios.post('api/token/refresh/',
      data
    ).then(response => {
      commit('setToken', response.access)
    });
  },
  tryLogIn({commit}, data) {
    return axios.post('api/token/',
      data
    ).then(response => {
      commit('setToken', response.access);
      commit('setRefresh', response.refresh);
      commit('setUser', response.user)
      return response;
    }).catch(response => {
      console.error(response);
    });
  },
  async refreshLogin({commit}){
    let token = localStorage.getItem('token')
    if(token) {
      axios.post('api/token/verify/',
        {'token': token}
      ).then(response => {
        commit('setToken', token);
      }).catch(response => {
        localStorage.removeItem('token')
        token = null
      })
    }
    return token;
  },
  async getProfile({commit}){
    let headers = {
      headers: {
        'AUTHORIZATION': `Bearer ${localStorage.getItem('token')}`
      }
    };
    return axios.get('api/users/my_profile', headers
    ).then(response => {
      commit('setUser', response)
      return response;
    }).catch(response => {
      console.error(response);
    });
  },

};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};
