# Thought Generation Is On-Device Only; Never a Cloud Call

Thoughts are generated locally, always. The live tier is the template
composer, paced by ThoughtService (one dispatch per 4 sim-seconds
globally, 15 per resident) and written only through
Store.dispatch("thought/set") after the snapshot validator approves
the text. The only generation tiers that may ever be added are the
on-device ones from the inner monologue design: WebLLM in a worker
behind an explicit download-consent toggle, and the browser's built-in
model where one is offered. Never add a paid API, an API key, a server
endpoint, or a free-tier cloud call. Generated text is display only;
the sim never waits for it and never reads it back as state.

Why: the page is public and static, so a key embedded in it is exposed
by definition, and every free cloud tier is capped and revocable. A
cloud dependency would give the feature an expiry date that neither
the player nor the project controls.
