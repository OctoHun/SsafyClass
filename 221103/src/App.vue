<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <button class="header-button mx-5 mt-5" @click="clickHome">Home</button>
    <button class="header-button" @click="clickStart">Start</button>
    <homeVue v-if="!isStarted"/>
    <noColor v-else-if="isStarted && page === 1" @click-left="clickLeft" @click-right="clickRight"/>
    <ssaFling v-else-if="isStarted && page === 2" @click-left="clickLeft" @click-right="clickRight"/>
    <ssaLeaf v-else-if="isStarted && page === 3" @click-left="clickLeft" @click-right="clickRight"/>
    <ssaFlower v-else-if="isStarted && page === 4" @click-left="clickLeft" @click-right="clickRight"/>
  </div>
</template>

<script>
import homeVue from '@/components/home'
import noColor from '@/components/Nocolor'
import ssaFling from '@/components/Ssafling'
import ssaLeaf from '@/components/Ssaleaf'
import ssaFlower from '@/components/Ssaflower'

export default {
  name: 'App',
  components: {
    homeVue,
    noColor,
    ssaFling,
    ssaLeaf,
    ssaFlower,
  },
  data: function () {
    return {
      page: 1,
      isStarted: false,
    }
  },
  methods: {
    clickHome: function () {
      this.isStarted = false
      this.page = 1
    },
    clickStart: function () {
      this.isStarted = true
    },
    clickLeft: function () {
      if (this.page === 1) {
        this.isStarted = false
      } else {
        this.page -= 1
      }
    },
    clickRight: function () {
      if (this.page === 4) {
        alert('Home으로 돌아갑니다!')
        this.page = 1
        this.isStarted = false
      } else {
        this.page += 1
      }
    }
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
.box-border {
  box-shadow: 2px 2px 2px 2px gray;
}
.side {
  width: 32px;
  height: 32px;
  border: 0px;
  background-color: white;
}
.ssafyimg {
  width: 159px;
  height: 157px;
}
</style>
