import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)
print(message.content)


"""
python quickstart.py
[TextBlock(citations=None, text='# Search terms for latest renewable energy developments:\n\n## Broad searches:\n- "renewable energy news 2024"\n- "clean energy breakthroughs"\n- "renewable energy innovations"\n\n## Technology-specific:\n- "solar panel efficiency improvements"\n- "offshore wind energy advances"\n- "green hydrogen developments"\n- "battery storage technology"\n- "perovskite solar cells"\n- "floating wind farms"\n\n## Policy & market:\n- "renewable energy investment trends"\n- "clean energy policy updates"\n- "net zero announcements"\n\n## Good sources to check:\n- **News**: Reuters Energy, Bloomberg Green, Canary Media\n- **Industry**: Renewable Energy World, PV Magazine, Wind Power Monthly\n- **Research**: Nature Energy, International Energy Agency (IEA) reports\n- **Organizations**: IRENA, NREL updates\n\n## Pro tips:\n- Add current year/month for freshness\n- Use Google News or set time filter to "Past month"\n- Follow hashtags like #RenewableEnergy #CleanTech on social media\n- Subscribe to industry newsletters for curated updates\n\nWhat specific aspect of renewable energy interests you most?', type='text')]  
"""