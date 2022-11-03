<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <button class="header-button mx-5 mt-5">Home</button>
    <button class="header-button">Start</button>
    <homeVue v-if="renderHome"/>
    <i class="fa-solid fa-circle-chevron-right"></i>
    <i class="fa-solid fa-circle-chevron-left"></i>
  </div>
</template>

<script>
import homeVue from '@/components/home'

export default {
  name: 'App',
  components: {
    homeVue,
  },
  data: function () {
    return {
      page: 1,
      isStarted: true,
    }
  },
  methods: {
  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.header-button {
  width: 100px;
  height: 50px;
  border: 1px solid rgb(255, 208, 0);
  background-color: white;
}
.box {
  width: 760px;
  height: 405px;
}
</style>
