/* Tailwind CDN theme: shared brand colours and fonts. */
tailwind.config = {
  theme: {
    extend: {
      colors: {
        navy: "#120B45",
        violet: "#3B1FA8",
        sun: "#FFC21A",
        coral: "#FF4D6D",
        mint: "#14D3A0",
        paper: "#FFF9EC",
        cloud: "#F1ECFF"
      },
      fontFamily: {
        display: ["Archivo", "system-ui", "sans-serif"],
        body: ["Hanken Grotesk", "system-ui", "sans-serif"],
        mono: ["IBM Plex Mono", "ui-monospace", "monospace"]
      }
    }
  }
};
