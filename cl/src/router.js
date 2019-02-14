import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: 'sample',
    routes: [
        {
            path: '/',
            redirect: '/decisionTree'
        },
        {
            path: '/decisionTree',
            name: 'decisionTree',
            component: () => import('./views/Sample1.vue')
        },
        {
            path: '/logisticRegression',
            name: 'logisticRegression',
            component: () => import('./views/Sample2.vue')
        },
    ]
})
