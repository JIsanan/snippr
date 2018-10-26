<template>
  <div class="">
    <div>
      <span class="icon">
        <font-awesome-icon icon="caret-up" />
      </span>
    </div>
    <div class="is-size-5">
      <strong>{{ upvotes }}</strong>
    </div>
    <div>
      <span class="icon">
        <font-awesome-icon icon="caret-down" />
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'source/plugins/axios';
export default {
  name: "VoteButtonSet",

  props: {
    hasUpvoted: {
      type: Boolean,
      required: true,
    },
    upvotes: {
      type: String,
      required: true,
    }
  },

  data() {
    return {
    };
  },
  computed: {
  },

  async mounted() {
    let headers = {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    };
    let languageFilter = this.languageFilter
    let query = 'http://127.0.0.1:8000/api/language/'
    let response = await axios.get(query, headers);
    this.languages = response;
  }
};
</script>

<style>

</style>
