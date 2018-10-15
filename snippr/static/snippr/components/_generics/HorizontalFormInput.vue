<template>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">{{ label }}</label>
    </div>
    <div class="field-body">
      <div class="field">
        <div class="control">
          <input
            v-if="type != 'textarea'"
            :placeholder="placeholder"
            :id="id"
              v-model="inputValue"
              v-bind="$attrs"
              :class="inputClass"
              v-on="listeners"
          >
          <textarea
            v-if="type === 'textarea'"
            :rows="rows"
            :placeholder="placeholder"
            :id="id"
              v-model="inputValue"
              v-bind="$attrs"
              :class="inputClass"
              v-on="listeners"
          ></textarea>
        </div>
      </div>
    </div>
	<slot name="right-addon"></slot>
  </div>
</template>

<script>

let counter = 0

export default {
  name: 'HorizontalFormInput',

  inheritAttrs: false,

  props: {
    rows: String,
    type: String,
    label: String,
    placeholder: String,
    value: {
      type: String,
      required: true,
    },
    id: {
      type: String,
      default() {
        return `form-field-${counter++}`;
      }
    },
    inputClass: String
  },

  computed: {
    listeners() {
      const { ...listeners } = this.$listeners;
      delete listeners.input;
      return listeners;
    },

    inputValue: {
      get(){
        return this.value;
      },

      set(value) {
        this.$emit('input', value);
      }
    }
  }
}
</script>

<style scoped lang="scss">

  .issue-input {
    margin-bottom: 2em;
  }

</style>
