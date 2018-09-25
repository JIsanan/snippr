<template>
    <div class="container">
    	<div class="content-description">
    		<h1 class="title">snippr</h1>
    		<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ullamcorper sapien eget felis auctor, vel fermentum erat tempor. Maecenas efficitur, mauris eget efficitur imperdiet, lacus augue sodales leo, non iaculis quam lorem id neque. Pellentesque sollicitudin libero nec sodales rhoncus. Vivamus vel sapien in neque pretium hendrerit. Fusce sed placerat eros. Ut interdum, ante eget venenatis cursus, nisl erat commodo justo, eu vulputate lacus augue a purus. Aenean hendrerit lorem quis ipsum convallis gravida. Curabitur condimentum ut leo eu varius. In purus dolor, interdum et massa eu, vulputate varius enim.</p>
    	</div>
    	<div class="content-login">
    		<div>
    			<button class="tab-button">Sign In</button><button class="tab-button">Register</button>
    		</div>
    		<form class="login-form">
    			<label>Username or Email</label>
    			<input type="text"/>
    			<label>Password</label>
    			<input type="password"/>
    			<div class="login-submit">
    				<input type="submit" value="Login" class="submit"/>
    				<a class="forgot-password">Forgot your password?</a>
    			</div>
    		</form>
    	</div>
    </div>
</template>

<script>
    export default {
        name: 'HomePage',
    }
</script>

<style scoped lang="scss">

    @import 'source/stylesheets//variables.scss';

    .container {
    	width: 100%;
    	display: flex;
    	justify-content: center;
    	align-items: center;
    	flex-direction: row;
    	flex-wrap: wrap;

    	.content-description {
    		margin: 12px;

			@media #{$hi-res} {
                width: 600px;
            }

            @media #{$laptop-large} {
                width: 400px;
            }

            @media #{$laptop} {
                width: 0 24px;
            }

            @media #{$tablet} {
                width: 0 20px;
            }

            @media #{$mobile} {
                width: 300px;
            }

    		.title {
    			font-family: $display-font;
    		}

    	}

    	.content-login {
    		width: 400px;
    		margin: 12px;

    		.tab-button {
    			background: transparent;
    			border: 1px solid #f1f1f1;
    			border-bottom: none;
    			padding: 16px 32px;
    			font-size: 16px;

    			&:hover {
    				background: #f1f1f1;
    			}
	    	}

    		.login-form {
				display: flex;
	    		flex-direction: column;
	    		padding: 24px;
	    		border: 1px solid #f1f1f1;

	    		label {
	    			margin-top: 18px;
	    		}

	    		input[type="text"],
	    		input[type="password"] {
	    			border: 1px solid #f1f1f1;
	    			padding: 8px 12px;
	    			font-size: 14px;
	    		}

	    		input[type="submit"], .button{
	    			background-color: transparent;
	    			border: 1px solid #f1f1f1;
	    			padding: 8px 12px;
	    			border-radius: 4px;
	    			width: 100%;

	    			&.submit {
	    				background: #43A047;
	    				color: white;
	    			}
	    		}

	    		.login-submit {
	    			display: flex;
	    			width: 100%;
	    			margin-top: 40px;
	    			flex-direction: column;
	    			justify-content: center;
	    			align-items: center;

	    			.forgot-password {
	    				margin-top: 12px;
	    			}

	    		}
    		}
    	}
    }
</style>