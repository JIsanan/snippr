import axios from 'axios';
const instance = axios.create({
    baseURL: window.location.origin,
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    },
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken'
});

instance.interceptors.request.use(function (config) {
	const token = this.$store.getters.token;
	this.$store.dispatch('auth/verifyJWT', {token});
	alert('test');
}, function (error) {
	return Promise.reject("something");
});

instance.interceptors.response.use(
    response => Promise.resolve(response.data),
    error => Promise.reject(error)
);

export default instance;
