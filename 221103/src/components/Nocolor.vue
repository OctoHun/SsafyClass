<template>
  <div>
    <div class="box box-border mx-auto mt-5 pt-1">
      <h2 class="mt-3">시작</h2>
      <div class="images mt-5">
        <button class="fa-solid fa-circle-chevron-left fa-2x side float-start ms-5 mt-5" @click="clickLeft"></button>
        <img src="../assets/ssanocolor.png" alt="" class="mx-5 ssafyimg">
        <button class="fa-solid fa-circle-chevron-right fa-2x side float-end me-5 mt-5" @click="clickRight"></button>
      </div>
      <h2 class="mt-5">싸플링(무색)</h2>
    </div>
  </div>
</template>
<script>
export default {
  name: 'noColor',
  methods: {
    clickLeft: function () {
      this.$emit('click-left')
    },
    clickRight: function () {
      this.$emit('click-right')
    }
  }
}
</script>

<style>

</style>