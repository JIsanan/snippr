import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [{
    path: '/',
    component: () => import('source/pages/HomePage.vue'),
    name: 'home',
    meta: {
        loginRequired: false
    }
},
{
	path: '/feed',
    component: () => import('source/pages/MainFeed.vue'),
    name: 'feed',
    meta: {
        loginRequired: false
    }
},
{
	path: '/createissue',
    component: () => import('source/pages/CreateIssue.vue'),
    name: 'createissue',
    meta: {
        loginRequired: false
    }
}];

const router = new VueRouter({
    routes,
    mode: 'history'
});

export default router;
