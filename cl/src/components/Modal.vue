<template>
  <div v-if="isShown" class="modal is-active" @click="isShown = false">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="modal-card" style="width:300px;">
        <section
          class="modal-card-body"
          style="height:50%;"
        >予測した結果は
          <br>
          <strong v-for="estimatedValue in estimatedValues" :key="estimatedValue">
            {{estimatedValue}}
            <br>
          </strong>
          です。
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
      estimatedValues: []
    };
  },
  computed: {
    labelString: function() {
      return this.labels.join(",");
    }
  },
  methods: {
    show: function(estimatedValues, labels) {
      this.estimatedValues = estimatedValues;
      this.labels = labels;
      this.isShown = true;
    }
  }
};
</script>

<style lang="scss">
</style>
