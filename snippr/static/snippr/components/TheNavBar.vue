<template>
  <nav class="navbar has-background-primary" role="navigation" aria-label="main navigation">
    <div class="container is-fluid">
      <div class="navbar-brand">
        <div class="navbar-item">
          <router-link class="has-text-white" :to="{ name: 'feed' }"">
          	<p class="is-size-4">
            	<strong>snippr</strong>
        	</p>
          </router-link>
        </div>
      </div>
          <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Register</strong>
          </a>
          <a class="button is-light">
            Sign in
          </a>
        </div>
      </div>
    </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TheNavBar'
}
</script>

<style>

</style>
