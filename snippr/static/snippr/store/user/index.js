import axios from 'source/plugins/axios';
import router from 'source/router/index';

const state = {

};

const getters = {

};

const mutations = {

};

const actions = {
  getUserProfile({commit}, data) {
    let headers = {
      headers: {
        'AUTHORIZATION': `Bearer ${localStorage.getItem('token')}`
      }
    };
    return axios.get(`https://1b7c4ba8.ngrok.io/api/users/${data}`, headers).then(response => {
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
