<template>
		<div class="columns is-centered feed">
				<div class="column is-8">
						<div class="columns is-marginless">
							<div class="column is-3 is-paddingless">
							</div>
							<div class="column is-paddingless">
								<div class="buttons is-right">
									<router-link :to="{ name: 'createissue' }" class="button is-danger is-outlined">Report Abuse</router-link>
									<router-link :to="{ name: 'createissue' }" class="button is-success is-outlined">Answer</router-link>
								</div>
							</div>
						</div>
						<hr>
						<div class="columns">
							<div class="column search-bar has-background-light">
								<FormInput
									type="text"
									class="has-addons"
									placeholder="Search"
									v-bind:value="search"
									inputClass="input"
									v-model="search"
									>
									<div slot="right-addon" class="control">
										<span class="select">
											<select>
												<option>Select dropdown</option>
												<option>With options</option>
											</select>
										</span>
									</div>
								</FormInput>
							</div>
						</div>
				</div>
		</div>
</template>

<script>
		import FormInput from '../components/_generics/FormInput.vue'
		export default {
				name: 'IssueDetails',

				components: {
						FormInput,
				},

				data () {
						return {
							tabOption: 0,
							search: '',
							searchType: '',
						}
				 },
				 methods: {
						isRegister () {
								this.register = true
						},
						isSignin () {
								this.register = false
						}
					}
		}
</script>

<style scoped>
		.feed {
				padding-top: 2rem;
		}
		.tabs {
				margin-bottom: 0px;

				.tab-item {
						margin-right: 8px;
				}
		}

		.search-bar {
				margin: 12px;
		}

		.vertical {
				flex-direction: column;
		}

		.flex-right {
				align-items: flex-end   !important;
		}

		.flex-vertical-center {
				display: flex;
				align-items: center;
		}

		.has-bottom-border {
				border-bottom: 1px solid hsl(0, 0%, 86%);
		}
</style>