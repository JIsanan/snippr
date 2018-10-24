import axios from 'axios';
import store from 'source/store/index';
const instance = axios.create({
    baseURL: window.location.origin,
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    },
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken'
});

instance.interceptors.request.use(function (config) {
	return config;
}, function (error) {
	return Promise.reject("something");
});

instance.interceptors.response.use(
    response => Promise.resolve(response.data),
    error => Promise.reject(error)
);

export default instance;
