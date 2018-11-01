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
        loginRequired: true
    }
},
{
    path: '/settings',
    component: () => import('source/pages/UserSettings.vue'),
    name: 'settings',
    meta: {
        loginRequired: true
    }
},
{
	path: '/createissue',
    component: () => import('source/pages/CreateIssue.vue'),
    name: 'createissue',
    meta: {
        loginRequired: true
    }
},
{
    path: '/issue/:id',
    component: () => import('source/pages/IssueDetails.vue'),
    name: 'issue',
    meta: {
        loginRequired: true
    }
},
{
    path: '/users/:id',
    component: () => import('source/pages/UserProfile.vue'),
    name: 'user',
    meta: {
        loginRequired: true
    }
},
{
    path: '/answer/:id',
    component: () => import('source/pages/Answer.vue'),
    name: 'answer',
    meta: {
        loginRequired: true
    },
    props: (route) => ({ query: route.query.c })
},];

const router = new VueRouter({
    routes,
    mode: 'history'
});

export default router;
