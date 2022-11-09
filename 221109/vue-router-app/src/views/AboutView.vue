<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">Home</router-link>
    <button @click="toHome">홈으로</button>
    <input type="text" @keyup.enter="gotohello" v-model="name">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data: function () {
    return {
      name: '',
    }
  },
  methods : {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    gotohello() {
      this.$router.push({name: 'hello', params: {userName: this.name}})
    }
  }
}
</script>