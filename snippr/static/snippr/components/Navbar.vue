<template>
    <nav
        v-show="isVisible"
        id="site-navbar"
        :class="{ 'transparent-navbar' : isTransparent }"
        class="the-navbar"
    >
        <div class="container">
        </div>
    </nav>
</template>

<script>
    import {mapState, mapActions, mapGetters, mapMutations} from 'vuex';

    export default {
        name: 'TheNavbar',

        components: {

        },

    };

</script>

<style scoped lang="scss">

    @import 'source/stylesheets/sass/abstract/variables.scss';
    @import 'source/stylesheets/sass/abstract/mixins.scss';
    .transparent-navbar {
        background: none !important;
        box-shadow: none !important;
    }

    #site-navbar {
        height: 56px;
        width: 100%;
        background: $accent-color;
        box-shadow: $nav-shadow;
        z-index: 500;
        position: fixed;
        transition-duration: .2s;

        .container {
            @include flex-align-center();
            height: inherit;

            @media #{$laptop} {
                padding: 0 48px;
            }

            @media #{$tablet} {
                padding: 0 32px;
            }

            @media #{$mobile} {
                padding: 0 16px;
            }
        }

        .navbar-left,
        .navbar-right {
            flex: 1;
            @include flex-align-center();
        }

        .navbar-center {
            @include flex-align-center();
        }

        .navbar-right {
            justify-content: flex-end;
        }

        .navbar-image img {
            padding-top: 4px;
            height: 48px;
        }

        .navbar-currency {
            width: 56px;

            @media #{$mobile} {
                display: none;
            }
        }

        .navbar-tabs {
            @include flex-align-center();

            .active > a {
                border-bottom: 2px solid $white;

                &:hover {
                    background: transparent;
                }
            }

            .new {
                a:after {
                    @include width-height(8px);
                    display: inline-block;
                    content: '';
                    background: $light-green;
                    border-radius: 50%;
                    margin-left: 8px;

                    @media #{$tablet} {
                        margin-left: 4px;
                    }
                }
            }

            a {
                @include flex-align-center();
                height: 56px;
                color: $white;
                padding: 0 16px;
                border-bottom: 2px solid transparent;
                text-decoration: none;
                transition-duration: .2s;

                &:hover {
                    background: rgba($white, .1);
                    border-bottom: 2px solid $white;
                }

                @media #{$tablet} {
                    padding: 0 8px;
                }
            }

            i {
                font-size: 20px;

                + span {
                    margin-left: 4px;

                    @media #{$tablet} {
                        display: none;
                    }
                }
            }
        }

        .navbar-button {
            position: relative;
            margin-left: 8px;

            &.icon {
                background: transparent;
                padding: 0 4px;
                height: 32px;
                transition-duration: .2s;
                color: $white;

                i {
                    font-size: 24px;
                }
            }

            .badge {
                @include flex-align-justify-center();
                height: 14px;
                min-width: 14px;
                padding: 0 4px;
                position: absolute;
                top: 0;
                right: 0;
                background: $red;
                font-size: 10px;
                border-radius: 12px;
            }

            &.profile-avatar {
                background: transparent;
                height: 32px;
                padding: 0;
                margin-left: 16px;

                .avatar {
                    @include width-height(32px);
                    border: 1px solid $white;
                }
            }
        }

        &.light {
            background: none;

            p {
                color: $gray-25;
            }
        }
    }
</style>