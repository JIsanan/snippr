import axios from 'source/plugins/axios';
import router from 'source/router/index';

const state = {

};

const getters = {
  getToken(){

  }
};

const mutations = {

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
    return "success";
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};
