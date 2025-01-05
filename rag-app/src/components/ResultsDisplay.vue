<template>
  <div v-if="answer">
    <h2>Answer</h2>
    <p>{{ answer }}</p>
  </div>
</template>

<script>
export default {
  props: {
    answer: String,
  },
}
</script>

<style scoped>
p {
  font-size: 1.2em;
}
</style>
