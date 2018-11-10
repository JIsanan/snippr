<template>
  <div class="columns snippet">
    <div class="column is-flex level is-marginless">
      <article class="media flex-vertical-center">
        <div class="media-left">
          <div class="level is-marginless">
            <div class="level-item vertical has-text-centered">
              <p class="subheading">
                <strong>{{ snippet.upvotes }}</strong>
              </p>
              <p class="heading is-marginless">
                upvotes
              </p>
            </div>
          </div>
        </div>
        <div class="media-content">
          <div class="content">
            <div class="title is-size-5">
              <span 
               :class="['tag',
                        {'is-success': snippet.status == 'Open'},
                        {'is-light': snippet.status == 'Closed'}
                       ]" >
                {{ snippet.status }}
              </span>
              <router-link :to="{name: 'issue', params: { id: snippet.pk }}" class="has-text-primary">
                <strong>{{ snippet.title }}</strong>
              </router-link>
            </div>
            <p class="subtitle is-size-6">
              <small>Opened {{ timestamp(snippet.date_created) }} by</small>
              <router-link :to="{name:'user', params: {id:snippet.user_id} }"><small>{{ snippet.username }}</small></router-link>
              <span class="tag is-light">{{ snippet.language_name }}</span>
            </p>
          </div>
        </div>
      </article>
    </div>
    <div class="column is-3 is-flex level is-marginless">
      <div class="level-item vertical flex-right">
        <span class="flex-vertical-center">
          <span class="icon">
            <font-awesome-icon icon="comment-alt" />
          </span>
          <span>{{ snippet.tracking_count }}</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "source/plugins/axios";
import moment from "moment";

import VoteButtonSet from "../_generics/VoteButtonSet.vue";

export default {
  name: "SnippetRow",

  components: {
    VoteButtonSet
  },

  props: {
    snippet: {
      type: Object,
      required: true
    }
  },

  data() {
    return {};
  },
  methods: {
    timestamp(date) {
      return moment(date, moment.ISO_8601).fromNow();
    }
  },
  async mounted() {}
};
</script>

<style scoped lang="scss">
.snippet {
  &:not(:last-child) {
    border-bottom: 1px solid hsl(0, 0%, 86%);
  }
}

.flex-right {
  align-items: flex-end !important;
}

.vertical {
  flex-direction: column;
}

.flex-vertical-center {
  display: flex;
  align-items: center;
}
</style>
