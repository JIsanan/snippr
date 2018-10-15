<template>
  <div class="field">
    <label class="label">{{ label }}</label>
    <div class="control is-expanded">
		<input
		  :placeholder="placeholder"
		  :id="id"
	      v-model="inputValue"
	      v-bind="$attrs"
	      :class="inputClass"
	      v-on="listeners"
		>
	</div>
	<slot name="right-addon"></slot>
  </div>
</template>

<script>

let counter = 0

export default {
  name: 'FormInput',

  inheritAttrs: false,

  props: {
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

</style>
