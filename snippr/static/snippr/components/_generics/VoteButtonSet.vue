<template>
  <div class="voteSet">
    <button class="button upvote is-medium" @click="upvote">
      <span :class="['icon', {'has-text-success': hasUpvoted}]">
        <font-awesome-icon icon="arrow-alt-circle-up" />
      </span>
    </button>
    <p class="is-size-4 vote">
      <strong>{{ upvotes }}</strong>
    </p>
    <button :class="['button', 'downvote', 'is-medium']" @click="downvote">
      <span :class="['icon', {'has-text-success': hasDownvoted}]">
        <font-awesome-icon icon="arrow-alt-circle-down" />
      </span>
    </button>
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
    hasDownvoted: {
      type: Boolean,
      required: true,
    },
    upvotes: {
      type: Number,
      required: true,
    },
    issueId: {
      type: Number,
      required: true,
    }
  },

  data() {
    return {
    };
  },
  computed: {
  },
  methods: {
    async upvote() {
      let headers = {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      }
      let query = `http://127.0.0.1:8000/api/commit/${this.issueId}/upvote/`
      let response = await axios.get(query, headers);
      this.hasUpvoted = response.upvote;
      this.hasDownvoted = response.downvote;
      this.upvotes = response.upvote_count;
    },
    async downvote() {
      let headers = {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      }
      let query = `http://127.0.0.1:8000/api/commit/${this.issueId}/downvote/`
      let response = await axios.get(query, headers);
      this.hasUpvoted = response.upvote;
      this.hasDownvoted = response.downvote;
      this.upvotes = response.upvote_count;
    },
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

<style scoped lang="scss">

  .upvote, .downvote {
    border: none;
    background: none;

    &:focus {
      border: none;
      box-shadow: none;
    }
    &:active {
      border: none;
    }
    &:hover {
      color: green;
    }
  }

  .voteSet {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .vote {
    font-size: 2rem;
    margin: 0px 4px;
  }
</style>
