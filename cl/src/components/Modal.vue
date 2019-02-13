<template>
  <div v-if="isShown" class="modal is-active" @click="isShown = false">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="modal-card">
        <section class="modal-card-body" stype="height:50%;">
          予測した結果は
          <strong>{{estimatedValue}}</strong>です。
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "modal",
  data() {
    return {
      isShown: false,
      labels: [],
      estimatedValue: ""
    };
  },
  computed: {
    labelString: function() {
      return this.labels.join(",");
    }
  },
  methods: {
    show: function(estimatedValue, labels) {
      this.estimatedValue = estimatedValue;
      this.labels = labels;
      this.isShown = true;
    }
  }
};
</script>

<style lang="scss">
</style>
