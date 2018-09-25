<template>
    <nav
        id="site-navbar"
    >
        <div class="container">
            <div class="logo"></div>
            <h1 class="title">snippr</h1>
        </div>
    </nav>
</template>

<script>
    import {mapState, mapActions, mapGetters, mapMutations} from 'vuex';

    export default {
        name: 'Navbar',

        components: {

        },

    };

</script>

<style scoped lang="scss">

    @import 'source/stylesheets//variables.scss';

    #site-navbar {
        height: 56px;
        width: 100%;
        background: #009688;
        box-shadow: 0px 2px 8px rgba(#F5F5F5, 0.5);
        z-index: 500;
        position: fixed;
        top: 0;
        left: 0;
        transition-duration: .2s;

        .container {
            display: flex;
            align-items: center;
            height: inherit;

            @media #{$hi-res} {
                padding: 0 20px;
            }

            @media #{$laptop-large} {
                padding: 0 20px;
            }

            @media #{$laptop} {
                padding: 0 24px;
            }

            @media #{$tablet} {
                padding: 0 20px;
            }

            @media #{$mobile} {
                padding: 0 16px;
            }

            .title {
                font-family: $display-font;
                color: white;
            }

            .logo {
                width: 40px;
                height: 40px;
                border: 1px solid black;
                border-radius: 50px;
                margin: 0px 8px;
            }
        }
    }
</style>