<template>
  <div>
    <HorizontalFormInput
      class="issue-input"
      type="textarea"
      label="Description"
      placeholder="My First Issue"
      :value="description"
      inputClass="textarea has-fixed-size"
      v-model="description"
      rows="5"
    />
    <HorizontalFormInput
      type="textarea"
      label="Code"
      v-model="code"
      :value="code"
      placeholder="My First Issue"
      inputClass="textarea has-fixed-size snippet"
      rows="5"
    />
    <button class="button is-success" @click="submit">Submit Answer</button>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions, mapMutations } from "vuex";
import HorizontalFormInput from "../components/_generics/HorizontalFormInput.vue";
export default {
  name: "Answer",
  components: {
    HorizontalFormInput
  },
  data() {
    return {
      code: "",
      description: "",
    }
  },
  methods: {
    async submit() {
      let payload = {
        description: this.description,
        code: this.code
      };

      let headers = {
        headers: {
          'AUTHORIZATION': `Bearer ${localStorage.getItem('token')}`
        }
      };

      let response = await axios.post(`http://127.0.0.1:8000/api/commit/${this.$route.params.id}/comment/`, payload, headers);
      console.log(response);
    }
  },
  mounted() {
    this.code = this.$route.query.c;
  }
};
</script>

<style scoped>
.app {
  min-height: 100vh;
}
</style>